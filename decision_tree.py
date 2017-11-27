from pandas import DataFrame
import pandas as pd
import math
class Dtree:
    def __init__(self):
        self.df=pd.read_csv('decision_examples.csv')
        self.space=self.df.shape[0]
    def calculate_space_entropy(self):
        positive=self.df[self.df['PlayTennis']=='Yes'].shape[0]
        negative=self.df[self.df['PlayTennis']=='No'].shape[0]
        self.entropy_space=-((float(positive)/self.space)*math.log((float(positive)/self.space),2))-((float(negative)/self.space)*math.log((float(negative)/self.space),2))
    def calculate_attribute_entropy(self,space,attribute,value):
        temp=space[space[attribute]==value]
        temp_length=temp.shape[0]
        positive=temp[temp['PlayTennis']=='Yes'].shape[0]
        negative=temp[temp['PlayTennis']=='No'].shape[0]
        if(positive and negative!=0):
            entropy_attribute=-((float(positive)/temp_length)*math.log((float(positive)/temp_length),2))-((float(negative)/temp_length)*math.log((float(negative)/temp_length),2))
        else:
            entropy_attribute=0
        return entropy_attribute
    def calculate_gain(self,space,attribute):
        #calculating gain of new space
        positive=space[space['PlayTennis']=='Yes'].shape[0]
        negative=space[space['PlayTennis']=='No'].shape[0]
        space_length=space.shape[0]
        entropy_space=-(float(positive)/space_length)*math.log((float(positive)/space_length),2)-(float(negative)/space_length)*math.log((float(negative)/space_length),2)

        out_values=space[attribute].unique()
        out1=out_values[0]
        entropy_out1=self.calculate_attribute_entropy(space,attribute,out1)
        out1_length=space[space[attribute]==out1].shape[0]
        out2=out_values[1]
        entropy_out2=self.calculate_attribute_entropy(space,attribute,out2)
        out2_length=space[space[attribute]==out2].shape[0]
        if(len(out_values)==3):
            out3=out_values[2]
            entropy_out3=self.calculate_attribute_entropy(space,attribute,out3)
            out3_length=space[space[attribute]==out3].shape[0]
            gain_attribute=entropy_space-((float(out1_length)/space_length)*entropy_out1+(float(out2_length)/space_length)*entropy_out2+(float(out3_length)/space_length)*entropy_out3)
        else:
            gain_attribute=entropy_space-((float(out1_length)/space_length)*entropy_out1+(float(out2_length)/space_length)*entropy_out2)
        return gain_attribute
    def calculate_gain_space(self,attribute):
        return self.calculate_gain(self.df,attribute)
    def calculate_gain_attribute_value(self,column,value,attribute):
        space_new=self.df[self.df[column]==value]
        positive=space_new[space_new['PlayTennis']=='Yes'].shape[0]
        negative=space_new[space_new['PlayTennis']=='No'].shape[0]
        if(positive!=0 and negative==0):
            result='Yes'
            return result
        elif(positive==0 and negative!=0):
            result='No'
            return result
        else:
            m=self.calculate_gain(space_new,attribute)
            return m
    def define_root(self):
        gain_outlook=self.calculate_gain_space('Outlook')
        gain_temperature=self.calculate_gain_space('Temperature')
        gain_humidity=self.calculate_gain_space('Humidity')
        gain_wind=self.calculate_gain_space('Wind')
        maxi=max(gain_wind,gain_humidity,gain_outlook,gain_temperature)
        if(maxi==gain_wind):
            self.root='Wind'
        elif(maxi==gain_outlook):
            self.root='Outlook'
        elif(maxi==gain_humidity):
            self.root='Humidity'
        else:
            self.root='Temperature'
    def next_level1(self):
        values=list(self.df[self.root].unique())
        print("values after root:")
        print(values)
        lst=['Wind','Humidity','Temperature']
        if(len(values)==3):
            j=2
        else:
            j=1
        gain_rain=[0]*3
        gain_overcast=[0]*3
        gain_sunny=[0]*3
        if(j==2):
            for i in range(3):
                if (lst[i]!=self.root) and j!=-1:
                    gain_rain[i]=self.calculate_gain_attribute_value(self.root,values[j],lst[i])

                else:
                    continue
            j-=1
        if(j==1):
            for i in range(3):
                if (lst[i]!=self.root) and j!=-1:
                    gain_overcast[i]=self.calculate_gain_attribute_value(self.root,values[j],lst[i])

                else:
                    continue
            j-=1
        if(j==0):
            for i in range(3):
                if (lst[i]!=self.root) and j!=-1:
                    gain_sunny[i]=self.calculate_gain_attribute_value(self.root,values[j],lst[i])

                else:
                    continue
            j-=1
        self.nextlevel1=[]
        for i in [0,1,2]:
            if(max(gain_sunny)==gain_sunny[i] and gain_sunny[i]):
                self.nextlevel1.append(lst[i])
            else:
                continue

        if(gain_overcast[0]!='Yes' or gain_overcast[1]!='Yes' or gain_overcast[2]!='Yes'):
            for i in [0,1,2]:
                if(max(gain_overcast)==gain_overcast[i] and gain_overcast[i]):
                    self.nextlevel1.append(lst[i])
                else:
                    continue
        else:
            self.nextlevel1.append('Yes')

        for i in [0,1,2]:
            if(max(gain_rain)==gain_rain[i] and gain_rain[i]):
                self.nextlevel1.append(lst[i])
            else:
                continue
    def next_level2(self):
        new_lst=[]
        self.final_play=[]
        for item in self.nextlevel1:
            if(item!='Yes'):
                new_lst.append(item)
        values0=self.df[new_lst[0]].unique()
        for k in range(len(values0)):
            space_new1=self.df[self.df[self.root]=='Sunny']
            space_new2=space_new1[space_new1[new_lst[0]]==values0[k]]
            self.final_play.append(list(space_new2['PlayTennis'].unique()))

        values1=self.df[new_lst[1]].unique()
        for k in range(len(values1)):
            space_new1=self.df[self.df[self.root]=='Rain']
            space_new2=space_new1[space_new1[new_lst[1]]==values1[k]]
            self.final_play.append(list(space_new2['PlayTennis'].unique()))

        print new_lst[0],"->",values0[0],":",self.final_play[0]
        print new_lst[0],"->",values0[1],":",self.final_play[1]
        print new_lst[1],"->",values1[0],":",self.final_play[2]
        print new_lst[1],"->",values1[1],":",self.final_play[3]


if __name__ == '__main__':
    s=Dtree()
    s.calculate_space_entropy()
    print("the entropy of space is:")
    print(s.entropy_space)
    s.define_root()
    print("the root is:")
    print(s.root)
    s.next_level1()
    print("the corresponding first next levels are:")
    print(s.nextlevel1)
    print("the coresponding second next levels are:")
    s.next_level2()

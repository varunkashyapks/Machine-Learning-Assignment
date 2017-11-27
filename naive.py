import pandas as pd
class Naive:
	def __init__(self):
		self.df=pd.read_csv("training_examples1.csv")
		self.space=self.df.shape[0]
	def classify(self):
		positive=self.df[self.df['PlayTennis']=='yes']
		negative=self.df[self.df["PlayTennis"]=="no"]
		pos1=positive[positive["Outlook"]=="sunny"].shape[0]
		pos2=positive[positive["Temp"]=="cool"].shape[0]
		pos3=positive[positive["Humidity"]=="high"].shape[0]
		pos4=positive[positive["Wind"]=="strong"].shape[0]
		self.allpos=[(float(pos1)/positive.shape[0]),(float(pos2)/positive.shape[0]),(float(pos3)/positive.shape[0]),(float(pos4)/positive.shape[0])]

		neg1=negative[negative["Outlook"]=="sunny"].shape[0]
		neg2=negative[negative["Temp"]=="cool"].shape[0]
		neg3=negative[negative["Humidity"]=="high"].shape[0]
		neg4=negative[negative["Wind"]=="strong"].shape[0]
		self.allneg=[(float(neg1)/negative.shape[0]),(float(neg2)/negative.shape[0]),(float(neg3)/negative.shape[0]),(float(neg4)/negative.shape[0])]
	def final(self):
		positive=self.df[self.df["PlayTennis"]=="yes"].shape[0]
		negative=self.df[self.df["PlayTennis"]=="no"].shape[0]
		map_pos=(float(positive)/self.space)*(self.allpos[0])*(self.allpos[1])*(self.allpos[2])*(self.allpos[3])

		map_neg=(float(negative)/self.space)*(self.allneg[0])*(self.allneg[1])*(self.allneg[2])*(self.allneg[3])

		self.total_map_pos=map_pos/(map_pos+map_neg)
		self.total_map_neg=map_neg/(map_pos+map_neg)

if __name__ == '__main__':
	s=Naive()
	s.classify()
	s.final()
	k=max(s.total_map_neg,s.total_map_pos)
	if k==s.total_map_pos:
		print"The PlayTennis is yes with map",s.total_map_pos
	else:
		print"The PlayTennis is no with map",s.total_map_neg
	print "The positive map output after normalising:",s.total_map_pos
	print "The negative map output after normalising:",s.total_map_neg

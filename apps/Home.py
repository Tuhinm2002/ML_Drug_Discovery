import streamlit as st
import os
from padelpy import from_smiles
import numpy as np
import pickle
import pandas as pd
from PIL import Image

def app():
		image = Image.open('logo.png')
		st.image(image,use_column_width=True)
		file = st.file_uploader("Upload",type=["csv"])
		if file:
			X = pd.read_csv(file)
			X = X['canonical_smiles']
			st.write(X)
			X_np = np.asarray(X)
			a = []
			for i in X_np:
				a.append(i)
			choose = st.selectbox("Choose", ("Hiv", "Alzheimer", "Lungs Cancer", "Chronic Kidney Disease", "Hepatitis c",
												"CoronaVirus","Leukemia","Hepatitis B","Influenza A",
												"Influenza B"), key=2)
			btn1 = st.button('Create Descripter',key=1)
			
			global res
			if choose == "CoronaVirus":
				if btn1:
					from_smiles(a,output_csv='descripter.csv',fingerprints=True,descriptors=False)
					input_x = pd.read_csv('descripter.csv')
					input_x = input_x.drop(columns=['Name'],axis=1)
					st.write(input_x)
					model = pickle.load(open('corona_model.pkl','rb'))
					global res
					res = model.predict(input_x)
					df = pd.concat([X,pd.DataFrame(res)],axis=1)
					st.markdown("""### Predicted IC50 VALUES""")
					st.write(df)
					os.remove('descripter.csv')
					st.session_state["value"] = "CoronaVirus"

			elif choose == "Hepatitis C":
				if btn1:
					from_smiles(a,output_csv='descripter.csv',fingerprints=True,descriptors=False)
					input_x = pd.read_csv('descripter.csv')
					input_x = input_x.drop(columns=['Name'],axis=1)
					st.write(input_x)
					model = pickle.load(open('hepatitisC_model.pkl','rb'))
					global res
					res = model.predict(input_x)
					df = pd.concat([X,pd.DataFrame(res)],axis=1)
					st.markdown("""### Predicted IC50 VALUES""")
					st.write(df)
					os.remove('descripter.csv')
					st.session_state["value"] = "Hepatitis C"

			elif choose == "Hepatitis B":
					if btn1:
						from_smiles(a,output_csv='descripter.csv',fingerprints=True,descriptors=False)
						input_x = pd.read_csv('descripter.csv')
						input_x = input_x.drop(columns=['Name'],axis=1)
						st.write(input_x)
						model = pickle.load(open('hepatitisB_model.pkl','rb'))
						global res
						res = model.predict(input_x)
						df = pd.concat([X,pd.DataFrame(res)],axis=1)
						st.markdown("""### Predicted IC50 VALUES""")
						st.write(df)
						os.remove('descripter.csv')
						st.session_state["value"] = "Hepatitis B"

			elif choose == "Aromatase":
					if btn1:
						from_smiles(a,output_csv='descripter.csv',fingerprints=True,descriptors=False)
						input_x = pd.read_csv('descripter.csv')
						input_x = input_x.drop(columns=['Name'],axis=1)
						st.write(input_x)
						model = pickle.load(open('aromatase_model.pkl','rb'))
						global res
						res = model.predict(input_x)
						df = pd.concat([X,pd.DataFrame(res)],axis=1)
						st.markdown("""### Predicted IC50 VALUES""")
						st.write(df)
						os.remove('descripter.csv')
						st.session_state["value"] = "Aromatase"

			elif choose == "Lungs Cancer":
					if btn1:
						from_smiles(a,output_csv='descripter.csv',fingerprints=True,descriptors=False)
						input_x = pd.read_csv('descripter.csv')
						input_x = input_x.drop(columns=['Name'],axis=1)
						st.write(input_x)
						model = pickle.load(open('lungs_model.pkl','rb'))
						global res
						res = model.predict(input_x)
						df = pd.concat([X,pd.DataFrame(res)],axis=1)
						st.markdown("""### Predicted IC50 VALUES""")
						st.write(df)
						os.remove('descripter.csv')
						st.session_state["value"] = "Lungs Cancer"

			elif choose == "Dengue":
					if btn1:
						from_smiles(a,output_csv='descripter.csv',fingerprints=True,descriptors=False)
					input_x = pd.read_csv('descripter.csv')
					input_x = input_x.drop(columns=['Name'],axis=1)
					st.write(input_x)
					model = pickle.load(open('dengue_model.pkl','rb'))
					global res
					res = model.predict(input_x)
					df = pd.concat([X,pd.DataFrame(res)],axis=1)
					st.markdown("""### Predicted IC50 VALUES""")
					st.write(df)
					os.remove('descripter.csv')
					st.session_state["value"] = "Dengue"

			elif choose == "Alzheimer":
					if btn1:
						from_smiles(a,output_csv='descripter.csv',fingerprints=True,descriptors=False)
						input_x = pd.read_csv('descripter.csv')
						input_x = input_x.drop(columns=['Name'],axis=1)
						st.write(input_x)
						model = pickle.load(open('alzheimer_model.pkl','rb'))
						global res
						res = model.predict(input_x)
						df = pd.concat([X,pd.DataFrame(res)],axis=1)
						st.markdown("""### Predicted IC50 VALUES""")
						st.write(df)
						os.remove('descripter.csv')
						st.session_state["value"] = "Alzheimer"

			elif choose == "Influenza A":
					if btn1:
						from_smiles(a,output_csv='descripter.csv',fingerprints=True,descriptors=False)
						input_x = pd.read_csv('descripter.csv')
						input_x = input_x.drop(columns=['Name'],axis=1)
						st.write(input_x)
						model = pickle.load(open('influenzaA_model.pkl','rb'))
						global res
						res = model.predict(input_x)
						df = pd.concat([X,pd.DataFrame(res)],axis=1)
						st.markdown("""### Predicted IC50 VALUES""")
						st.write(df)
						os.remove('descripter.csv')
						st.session_state["value"] = "Influenza A"

			elif choose == "Influenza B":
					if btn1:
						from_smiles(a,output_csv='descripter.csv',fingerprints=True,descriptors=False)
						input_x = pd.read_csv('descripter.csv')
						input_x = input_x.drop(columns=['Name'],axis=1)
						st.write(input_x)
						model = pickle.load(open('influenzaB_model.pkl','rb'))
						global res
						res = model.predict(input_x)
						df = pd.concat([X,pd.DataFrame(res)],axis=1)
						st.markdown("""### Predicted IC50 VALUES""")
						st.write(df)
						os.remove('descripter.csv')
						st.session_state["value"] = "Influenza B"

			elif choose == "Leukemia":
					if btn1:
						from_smiles(a,output_csv='descripter.csv',fingerprints=True,descriptors=False)
						input_x = pd.read_csv('descripter.csv')
						input_x = input_x.drop(columns=['Name'],axis=1)
						st.write(input_x)
						model = pickle.load(open('leukemia_model.pkl','rb'))
						global res
						res = model.predict(input_x)
						df = pd.concat([X,pd.DataFrame(res)],axis=1)
						st.markdown("""### Predicted IC50 VALUES""")
						st.write(df)
						os.remove('descripter.csv')
						st.session_state["value"] = "Leukemia"


		# image = Image.open('logo.png')
		# st.image(image,use_column_width=True)
		# file = st.file_uploader("Upload",type=["csv"])
		# if file:
		# 	X = pd.read_csv(file)
		# 	X = X['canonical_smiles']
		# 	st.write(X)
		# 	X_np = np.asarray(X)
		# 	a = []
		# 	for i in X_np:
		# 		a.append(i)
		# 	btn1 = st.button('Create Descripter',key=1)
		# 	if btn1:
		# 		from_smiles(a,output_csv='descripter.csv',fingerprints=True,descriptors=False)
		# 		input_x = pd.read_csv('descripter.csv')
		# 		input_x = input_x.drop(columns=['Name'],axis=1)
		# 		st.write(input_x)
		# 		model = pickle.load(open('trained_model.pkl','rb'))
		# 		global res
		# 		res = model.predict(input_x)
		# 		df = pd.concat([X,pd.DataFrame(res)],axis=1)
		# 		#df = df.iloc[1:,:]
		# 		st.markdown("""### Predicted IC50 VALUES""")
		# 		st.write(df)
		# 		#st.write(type(res))
		# 		os.remove('descripter.csv')


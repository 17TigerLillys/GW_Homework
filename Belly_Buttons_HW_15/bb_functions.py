#dependencies
import time
import pandas as pd
import json as json
import csv




def get_sample_names():
    print("names function")
    samples_df = pd.read_csv("DataSets/belly_button_biodiversity_samples.csv", encoding = "utf-8")
    sample_names_w_id = list(samples_df.columns.values)
    sample_names = sample_names_w_id[1:]
    return sample_names, samples_df

def get_OTU_desc():
    print("otu function")
    file_df = pd.read_csv("DataSets/belly_button_biodiversity_otu_id.csv", encoding = "utf-8")
    otu_data = list(file_df['lowest_taxonomic_unit_found'])
    return otu_data

def get_sample_metadata():
    print("metadata function")
    file_df = pd.read_csv("DataSets/Belly_Button_Biodiversity_Metadata.csv", encoding = "utf-8")
    sub_file_df = file_df[["SAMPLEID","ETHNICITY","GENDER","AGE","WFREQ","BBTYPE","LOCATION"]]
    #set the nAn values to either NA or 0
    values = {'ETHNICITY': "NA", 'GENDER': "NA", 'AGE': 0, 'WFREQ': 0,'BBTYPE': "NA", "LOCATION": "NA"}
    new_file_df = sub_file_df.fillna(value=values, inplace=True)
    new_file_df.set_index("SAMPLEID", inplace=True)
    meta_data = new_file_df.to_dict(orient='index')
    print(meta_data)
    return meta_data

def get_sample_values(sample):
    print("sample values function")
    samples_df = pd.read_csv("DataSets/belly_button_biodiversity_samples.csv", encoding = "utf-8")
    otu_df = pd.read_csv("DataSets/belly_button_biodiversity_otu_id.csv", encoding = "utf-8")
    sorted_sample_df = samples_df[['otu_id','BB_'+sample]]
    sorted_lists = sorted_sample_df.sort_values('BB_'+sample,ascending=False)
    sorted_lists.rename(columns={'BB_'+sample:'sample_values'}, inplace=True)

    #merge with OTU data to get the description
    merge_table = pd.merge(sorted_lists, otu_df, on="otu_id")
    merge_table.rename(columns={'lowest_taxonomic_unit_found':'otu_desc'}, inplace=True)

    #only get the top 10 samples after sorting
    #sorted_dict = merge_table[0:10].to_dict(orient='list')
    sorted_dict = merge_table[0:3673].to_dict(orient='list')
    sorted_list = [sorted_dict]

    return sorted_list




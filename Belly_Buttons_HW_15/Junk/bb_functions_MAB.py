#dependencies
import pandas as pd
import json as json
import csv




def get_sample_names():
    print("names function")

    samples_df = pd.read_csv("belly_button_biodiversity_samples.csv", encoding = "utf-8")
    sample_names_w_id = list(samples_df.columns.values)
    sample_names = sample_names_w_id[1:]
    return sample_names, samples_df

def get_OTU_desc():
    print("otu function")
    file_df = pd.read_csv("belly_button_biodiversity_otu_id.csv", encoding = "utf-8")
    otu_data = list(file_df['lowest_taxonomic_unit_found'])
    return otu_data

def get_sample_metadata():
    print("metadata function")
    file_df = pd.read_csv("Belly_Button_Biodiversity_Metadata.csv", encoding = "utf-8")
    file_df.set_index("SAMPLEID", inplace=True)
    meta_data = file_df.to_dict(orient='index')
    return meta_data

#def get_washing_freq():
    #print("metadata function")
    #return wfreq_data

def get_sample_values():
    print("sample values function")
    #return sample_data

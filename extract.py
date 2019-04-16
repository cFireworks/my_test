import xml.etree.ElementTree as ET
import numpy as np
import pandas as pd
import os
import sys


def extract_info(file_dir, action_list):
    samples = os.listdir(file_dir)
    samples_action = {}
    for file in samples:
        action_dic = dict(zip(action_list.tolist(), [0] * action_list.size))
        xml_file = os.path.join(file_dir, file)
        tree = ET.parse(xml_file)
        root = tree.getroot()
        for node in root.iter('action'):
            if 'api_name' not in node.attrib:
                continue
            else:
                api = node.attrib['api_name']
                if api in action_dic:
                    action_dic[api] += 1
        samples_action[file] = action_dic
    df = pd.DataFrame.from_dict(samples_action, orient='index')
    df.to_csv('out.csv')
    return


def extract_list(file_dir, action_list):
    action_num = []
    error_api = []
    for i in range(len(action_list)):
        action_num.append(i)
    dic_action = dict(zip(action_list, action_num))
    samples = os.listdir(file_dir)
    all_data = []
    samples_len = len(samples)
    for i, file in enumerate(samples):
        api_list = []
        xml_file = os.path.join(file_dir, file)
        tree = ET.parse(xml_file)
        root = tree.getroot()
        for node in root.iter('action'):
            if 'api_name' not in node.attrib:
                continue
            else:
                api = node.attrib['api_name']
                try:
                    api_list.append(dic_action[api])
                except Exception as e:
                    if api not in error_api:
                        error_api.append(api)
                        print(api, '  ', e)
        all_data.append(api_list)
        if i % 200 == 0:
            print(i, '/', samples_len)
    return all_data, error_api

def list2one_hot(file_list, action_list):
    max_length = len(action_list)
    results = []
    for single_list in file_list:
        single_result = np.zeros(shape=(len(single_list), max_length))
        for i, index in enumerate(single_list):
            single_result[i, index] = 1
        results.append(single_result)
    return results

def main(argv):
    if argv == None:
        print('argv is None')
    else:
        file_dir = argv[1]
        action_list = np.load('action_dic.npy')
        file_list = np.load(file_dir)
        results = list2one_hot(file_list, action_list)
        np.save(argv[2], np.array(results))


if __name__ == '__main__':
    main(sys.argv)

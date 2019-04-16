# my_test
action_dic是91个api名字的列表 <br>  
data是一个字典 data['item']是训练样本的api数字标号表示序列的列表，各序列长度未做删减  data['label']是标签 <br>
    
    import numpy as np
    
    data = np.load('data.npy')
    test_data = np.load('test_data_dic.npy')
    data_dic = data.item()
    test_data_dic = test_data.item()
    
extract.py 从xml文件中提取api调用信息<br>
    
    extract_info(file_dir, action_list) # 提取目录下样本，api字典中各api调用的数目，并导出到csv
    extract_list(file_dir, action_list) # 提取目录下样本，api调用的序列（仅记录api字典中的api）
    list2one_hot(file_list, action_list) # 将序列列表转为onehot表示的矩阵

# my_test
action_dic是91个api名字的列表 <br>  
data是一个字典 data['item']是训练样本的api数字标号表示序列的列表，各序列长度未做删减  data['label']是标签 <br>
'''python
    
    import numpy as np
    data = np.load('data.npy')
    test_data = np.load('test_data_dic.npy')
    data_dic = data.item()
    test_data_dic = test_data.item()
    
'''

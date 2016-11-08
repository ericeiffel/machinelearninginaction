# coding=utf-8
__author__ = 'chenjiao'

#稠密矩阵转libsvm
def data2libsvm(input_txt,output_txt,delimiter):
    txt = open(input_txt,'r')
    svm_data = open(output_txt,'w')
    for line in txt.readlines():
        features = line.split(delimiter)
        num = len(features)
        svm_format = features[-1].strip('\n')   #odps数据存在\n换行需要去除
        for i in range(0,num-1):
            svm_format = "%s %d:%s" % (svm_format,i+1,features[i])
        # svm_format = svm_format + '\n'
        svm_data.write(svm_format)
        print svm_format

#稀疏矩阵转libsvm
def sparse2libsvm(input_txt,output_txt):
    txt = open(input_txt,'r')
    svm_data = open(output_txt,'w')
    for line in txt.readlines():
        targetY=line.split(';')[0]
        features = line.split(';')[1].split(',')
        num = len(features)
        svm_format = targetY
        for i in range(0,num):
            svm_format = "%s %d:%s" % (svm_format,i+1,features[i].split(':')[1])
        # svm_format = svm_format + '\n'  #已经自动换行，去除该步骤
        svm_data.write(svm_format)
        print svm_format

#稀疏矩阵的特征获取
def feature2Id(input_txt,output_txt):
    txt = open(input_txt,'r')
    featureId = open(output_txt,'w')
    for line in txt.readlines():
        targetY=line.split(';')[0]
        features = line.split(';')[1].split(',')
        num = len(features)
        # svm_format = targetY
        for i in range(0,num):
            svm_format = "%d:%s\n" % (i+1,features[i].split(':')[0])
            featureId.write(svm_format)
            print(svm_format)
        # svm_format = svm_format + '\n'
        break


if __name__=='__main__':
    # origin_data_input='pai_temp_9190_163800_1.txt'
    # svm_data_output='temp.txt'
    # feature_id_output='temp1.txt'
    # #获取匣子的特征
    # feature2Id(origin_data_input,feature_id_output);
    data_input='chenjiao_tmp_data.txt'
    svm_data_output='temp2.txt'
    data2libsvm(data_input,svm_data_output,';')

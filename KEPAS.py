# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 11:08:04 2016

@author: YuKeji
"""
#用来抓取KEGG特定路径上所有基因序列


import time
#载入biopython的包
from Bio.KEGG.REST import kegg_link
from Bio.KEGG.REST import kegg_get
#载入正则表达式
import re 
#载入os，自动创建目录
import os
#定义用来将http response结果 转化成string类型的函数
def http_byte2string(response):
    response_read = response.read()
    response_byte2string =response_read.decode()
    return response_byte2string
#pathway作为输入   
pathway = input('Iput pathway ID: ')   

#用biopython内置函数kegg_link来获取pathway上所有的基因列表，为kegg的ID号
print('Retreving gene list . . .')
gene_list_with_pathway = kegg_link('genes',pathway)
#转换为string格式
gene_list_with_pathway_b2string = http_byte2string(gene_list_with_pathway)
#将string按照\t和\n的分隔符分开
gene_list_split = re.split('\n|\t', gene_list_with_pathway_b2string)
#对list切去偶数index的元素，得到pathway上所有基因的编号
gene_list = gene_list_split[1::2]
#历遍列表中的每个基因 用kegg_get抓取对应的序列，保存在相同的路径
for i in gene_list:
    dir2save = '/Users/YuKeji/Documents/Lab/RNAseq_Data/'+pathway
    os.makedirs(dir2save, exist_ok=True)
    time.sleep(0.4)
    gene_Seq = kegg_get(i, 'ntseq')
    print('Retreving Sequence . . .')
    gene_Seq_byte2string = http_byte2string(gene_Seq)
    gene_Seq_fasta = open(dir2save +'/'+i+'.fa','w')
    print('Writing Files . . .')
    gene_Seq_fasta.writelines(gene_Seq_byte2string)
    gene_Seq_fasta.close()
print('All done!')
'''
用cat 命令在bash下合并所有fasta文件
'''
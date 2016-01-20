# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 11:08:04 2016

@author: YuKeji
"""
#用来抓取特定路径上所有基因序列

#载入biopython的包
from Bio.KEGG.REST import kegg_link
from Bio.KEGG.REST import kegg_get
#定义用来将http response结果 转化成string类型的函数
def http_byte2string(response):
    response_read = response.read()
    response_byte2string =response_read.decode()
    return response_byte2string
#pathway作为输入   
pathway = input('Iput pathway ID: ')    

#用biopython内置函数kegg_link来获取pathway上所有的基因列表，为kegg的ID号
gene_list = kegg_link('genes',pathway)
print('Retreving gene list . . .')
#转换为string格式
gene_list_byte2string = http_byte2string(gene_list)
#写入txt
gene_txt = open('/Users/YuKeji/Documents/Lab/RNAseq_Data/KEGG_gene/'+pathway+'/'+pathway+'.txt','w')
print('Writing file . . .')
gene_txt.writelines(gene_list_byte2string)
gene_txt.close()
'''
运行到此，需要在相应文件路径下，将txt用EXCEL打开，另存为excel格式
'''
#读取含有kegg ID的column
import xlrd
book1 = xlrd.open_workbook('/Users/YuKeji/Documents/Lab/RNAseq_Data/KEGG_gene/'+pathway+'/'+pathway+'.xlsx')
sheet1 = book1.sheet_by_name(pathway)
genes_in_pathway = sheet1.col_values(1)

#历遍列表中的每个基因 用kegg_get抓取对应的序列，保存在相同的路径
for i in genes_in_pathway:
    gene_Seq = kegg_get(i, 'ntseq')
    print('Retreving Sequence . . .')
    gene_Seq_byte2string = http_byte2string(gene_Seq)
    gene_Seq_fasta = open('/Users/YuKeji/Documents/Lab/RNAseq_Data/KEGG_gene/'+pathway+'/'+i+'.fa','w')
    print('Writing Files . . .')
    gene_Seq_fasta.writelines(gene_Seq_byte2string)
    gene_Seq_fasta.close()
'''
用cat 命令在bash下合并所有fasta文件
'''
#coding:gbk

input = open("res_kaisa.txt",'r').read()


def jiema(n,pianyi):
	res = n + pianyi
	
	if n <= 90 and n >= 65:    #为了实现循环加法
		if res > 90:
			return 64 + res - 90
		return res 
	if n <= 122 and n >= 97:
		if res > 122:
			return 96 + res - 122
		return res
	

def main():
	list_res = []
	lis = list(input)
	for ele in lis:
		if ele.isalpha() is True:
			res = jiema(ord(ele),20)
			list_res.append(chr(res))
		else :
			list_res.append(ele)
	res = ''.join(list_res)
	print res
	output = open('res_kaisa1.txt','w')
	output.write(res)
	output.close()
	
if __name__ == '__main__':
	main()
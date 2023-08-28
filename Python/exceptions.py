# def divide(a,b):
#     return a/b
# try:
#   ans = print(divide(40,0))
    
# # except Exception as e:
# #    print('something went wrong', e)
# #    print(e.__class__)
# except ZeroDivisionError as e:
#    print(e, 'We cannot divide by zero')
   
# except Exception as e:
#    print(e, 'Something went wrong')

# items = [1,2,3,4,5]
# try:
#   item = items[6]
#   print(item)
# except Exception as e:
#   print('Item doesnot exist in the list', e)

try:
  with open('file.txt', 'r') as file:
    print(file.read())
except Exception as e:     
  print('The file couldnot be found', e)
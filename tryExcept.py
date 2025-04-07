try:
    print(x)
except NameError:
    print("Variabel is not defined")
except:
    print("Something else went wrong")
else: #else untuk tidak ada error
    print("nothing went wrong") 
finally: #ada eror atau tidak akan
    print("selalu tampil")

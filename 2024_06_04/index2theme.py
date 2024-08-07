from pprint import pprint
import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
import tools

class Window(ThemedTk):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.title("全台空氣品質指標(AQI)")
        #self.option_add("*Font","微軟正黑體 40")
        #定義style的名稱
        style = ttk.Style()

        # 14.52
        style.configure('Top.TFrame')
        style.configure('Top.TLabel',font=('Helvetica',25,'bold'))

        title_frame = ttk.Frame(self,style='Top.TFrame',borderwidth=2,relief='groove')
        ttk.Label(title_frame,text='全台空氣品質指標(AQI)@Lable',style='Top.TLabel').pack(expand=True,fill='y')
        title_frame.pack(ipadx=100,ipady=30,padx=10,pady=10)

        func_frame = ttk.Frame(self,style='Top.TFrame',borderwidth=1,relief='groove')
        ttk.Button(func_frame,text="AQI品質最好的5個",command=self.click1).pack(side='left',expand=True)
        ttk.Button(func_frame,text="AQI品質最差的5個",command=self.click2).pack(side='left',expand=True)
        ttk.Button(func_frame,text="pm2.5品質最好的5個",command=self.click3).pack(side='left',expand=True)
        ttk.Button(func_frame,text="pm2.5品質最好的5個",command=self.click4).pack(side='left',expand=True)
        func_frame.pack(ipadx=100,ipady=30,padx=10,pady=10)

    def click1(self):
        print("click1")
    
    def click2(self):
        print("click2")

    def click3(self):
        print("click3")
    
    def click4(self):
        print("click4")


        #15:00 ###########################
        # func_frame = ttk.Frame(self,style='Top.TFrame',borderwidth=1,relief='groove')
        # ttk.Button(func_frame,text="AQI品質最好的5個").pack(side='left',expand=True)
        # ttk.Button(func_frame,text="AQI品質最差的5個").pack(side='left',expand=True)
        # ttk.Button(func_frame,text="pm2.5品質最好的5個").pack(side='left',expand=True)
        # ttk.Button(func_frame,text="pm2.5品質最好的5個").pack(side='left',expand=True)
        # func_frame.pack(ipadx=100,ipady=30,padx=10,pady=10)

        # 14.30 ############################
        # style.configure('Top.TFrame',background='#BEC23F')
        # style.configure('Top.TLabel',font=('Helvetica',25))

        # title_frame = ttk.Frame(self,style='Top.TFrame')
        # ttk.Label(title_frame,text='全台空氣品質指標(AQI)',style='Top.TLabel').pack()
        # title_frame.pack(padx=100,pady=50)


def main():
    '''
    try:
        all_data:dict[any] = tools.download_json()
    except Exception as error:
        print(error)
    else:        
        data:list[dict] = tools.get_data(all_data)
        pprint(data)
    '''
    window = Window(theme="arc")
    window.mainloop()
    

if __name__ == '__main__':
    main()


# from pprint import pprint
# import tkinter as tk
# from tkinter import ttk
# from ttkthemes import ThemedTk
# # import tools

# class Window(ThemedTk):
#     def __init__(self,**kwargs):
#         super().__init__(**kwargs)
#         self.title("AQI顯示")
#         # self.option_add("*font")

#         ttk.Button(self, text="Quit", command=self.destroy).pack()


# def main():
#     '''
#     try:
#         all_data:dict[any] = tools.download_json()
#     except Exception as error:
#         print(error)
#     else:        
#         data:list[dict] = tools.get_data(all_data)
#         pprint(data)
#     '''
#     window = Window(theme="blue")
#     window.mainloop()
    

# if __name__ == '__main__':
#     main()
class Cash():
    

    def __init__(self):
        self.income = 0
        self.expenses = 0
        self.cash_flow = 0
        self.down_pay = 0
        self.clos_cost = 0
        self.re_bud = 0
        self.total_investment = 0
        self.annu_cash_flow = 0

    def invest(self):
            self.down_pay = int(input("Enter your down payment amount here: "))
            self.clos_cost = int(input("Enter closing cost amount here: "))
            self.re_bud = int(input("Enter any rehab budget amounts here: "))
            self.total_investment = self.down_pay + self.clos_cost + self.re_bud
            

    def flow(self):
        self.income = int(input("Enter your monthly rental income here: "))
        self.expenses = int(input("Enter your total monthly expenses here: "))
        self.cash_flow = (self.income - self.expenses) * 12
        self.annu_cash_flow = self.cash_flow  
        return self.cash_flow
    
    def calc(self):
        if self.total_investment != 0:
            return (self.annu_cash_flow / self.total_investment) * 100
        else:
             return 0 
         
         
        
       
money = Cash()
money.invest()
roi = money.flow()
print("ROI:", money.calc())

# I literally lost sleep over this, I'm not sure if I over simplified this, but in the end I got the same output as Brandon. Now back to watching python videos...

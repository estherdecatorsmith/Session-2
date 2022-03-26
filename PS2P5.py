
#include <iostream>
using namespace std;
int main()
{
int price,total,temp; //declare price,total,temp as integer variables
int dis_rate,dis_amt,tax,tax_amt; //declare dis_rate,dis_amt,tax,tax_amt as integer variables
cout<<"Enter the regular price of an item"<<endl; //display on the screen
cin>>price; //takes price as input from the user
cout<<"Enter the discount rate"<<endl; //display on the screen
cin>>dis_rate; //takes discount rate as input from the user
cout<<"Enter the tax rate"<<endl; //display on the screen
cin>>tax; //takes tax rate as input from the user
tax_amt=price*tax/100; //calculate tax amount taxamount=price*taxrate/100
price=price+tax_amt; //calculate total retail sale add tax amount from sale price of item
dis_amt=price*dis_rate/100; //calculate discount amount=price*discountrate/100
temp=price-dis_amt; //subtract discount amount from price temp=price-discountamount
cout<<"Sale price of an item-"<<temp<<endl; //display sale price on screen after subtract discount
cout<<"Discount amount-"<<dis_amt<<endl; //display Discount amount
cout<<"Tax amount-"<<tax_amt<<endl; //display tax amount
cout<<"Total retail sale-"<<price; //display retail sale
return 0;
}
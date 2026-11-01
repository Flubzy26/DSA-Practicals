#include<iostream>
using namespace std;
const int MAX=5;
class PizzaParlour
{
	int front,rear;
	int orders[MAX];
	public:
	PizzaParlour()
	{
		front=rear=-1;
	}
	int addOrder(int data);
	void serveOrder();
	void display();
};
int PizzaParlour::addOrder(int id)           
{
	if(rear==-1)
	{
		front=rear=0;
		orders[rear]=id;
		return 1;
	}
	else
	{
		int pos=(rear+1)%MAX;
		if(pos==front)
		{
			cout<<"\nCafe is Full.Please wait.\n";
			return 0;
		}
		else
		{
			rear=pos;
			orders[rear]=id;
			return true;
		}
	}
}

void PizzaParlour::serveOrder()              
{
	if(front==-1)
	{
		cout<<"\nDont serve no customer in Cafe.\n";
	}
	else
	{
		cout<<"\n Order No. "<<orders[front]<<" is served.\n";
		if(front==rear) 
		{
			front=rear=-1;
		}
		else	
		{
			front=(front+1)%MAX;
		}
	}
}

void PizzaParlour::display()                     
{
	int i=0;
	if(front==-1)
	{
		cout<<"\nCafe is Empty.No orders.\n";
		return;
	}
	else
	{
		cout<<"Order Id's:"<<endl;
		for(i=front;i!=rear;i=((i+1)%MAX))
		{
			cout<<orders[i]<<"  ";
		}
		cout<<orders[rear];
	}
}
int main()
{
	int ch,id=0;
	char ans;
	PizzaParlour p;

	do
	{
		cout<<"*****KBT cafe*****"<<endl;
		cout<<"****Menu*****"<<endl;
		cout<<"1.Please give your order\n2.Serve order are\n3.Display orders\n4.Exit\n";
		cout<<"Enter your choice";
		cin>>ch;

		switch(ch)
		{
			case 1:
				id++;
				if(p.addOrder(id))
				{
					cout<<"Thank you for order!!!"<<endl;
					cout<<"Your order id is : "<<id<<endl;
				}
				else
				{
					id--;
				}
				break;

			case 2:
				p.serveOrder();
				break;

			case 3: cout<<"The order remaning to serve are"<<endl;
				p.display();
				break;
			default:
	   			cout<<"Invalid choice"<<endl;  
		}
		cout<<"\nDo you want to continue"<<endl;
	        cin>>ans;
	   }while(ans=='y'||ans=='Y');
	   cout<<"\nThank You.Keep Visiting.";

}

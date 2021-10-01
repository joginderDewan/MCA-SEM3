import java.awt.*;
import javax.swing.*;
import java.applet.*;
import java.awt.event.*;
class CurrencyConveter extends JFrame implements ActionListener
{
JFrame f;
JLabel l1,l2;
JTextField t1,t2;
JButton b1,b2;
JComboBox c1,c2;

CurrencyConveter()
{
f=new JFrame("Currency Conveter");

String[] currency={"US Dollar","Indian Rupee","British Pound","Euro","Chinese Yuan"};
c1=new JComboBox(currency);
c1.setSelectedIndex(0);
c1=new JComboBox(currency);
//c2.setSelctedIndex(1);

l1=new JLabel("enter your currency");
l2=new JLabel("conveted currency is:");

CheckboxGroup g=new CheckboxGroup(); 
Checkbox i=new Checkbox("India",g,true);
Checkbox u=new Checkbox("usa",g,false);
Checkbox n=new Checkbox("Nepal",g,false);
Checkbox m=new Checkbox("Malaysia",g,false);

t1=new JTextField(10);
t2=new JTextField(10);

b1=new JButton("convert");
b2=new JButton("cancel");

f.setVisible(true);
f.setSize(400,400);
f.setLayout(new FlowLayout());

f.add(l1);
f.add(t1);
f.add(b1);
f.add(b2);
f.add(l2);
f.add(t2);

b1.addActionListener(this);
b2.addActionListener(this);

}
public void actionPerformed(ActionEvent e)
{
}

public static void main(String []pp)
{
new CurrencyConveter();
}

}

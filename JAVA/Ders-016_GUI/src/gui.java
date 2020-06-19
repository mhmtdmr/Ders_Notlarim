
import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
public class gui implements ActionListener  {

	public static void main(String[] args) {

		// Ana çerçeveyi oluşturma
        JFrame frame = new JFrame("İlk Grafik Arayüzlü Programımız");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(500,400);
        
        JPanel panel = new JPanel(); // the panel is not visible in output
        JLabel label = new JLabel("Enter Text");
        JTextField tf = new JTextField(10); // accepts upto 10 characters
        JButton send = new JButton("Send");
 
        
        
        
        JButton reset = new JButton("Reset");
        panel.add(label); // Components Added using Flow Layout
        panel.add(tf);
        panel.add(send);
        panel.add(reset);
        
        //Menü ve bileşenlerini ekleme
        JMenuBar mb = new JMenuBar();
        JMenu m1 = new JMenu("Dosya");
        JMenu m2 = new JMenu("Yardım");
        mb.add(m1);
        mb.add(m2);
        JMenuItem m11 = new JMenuItem("Aç");
        JMenuItem m22 = new JMenuItem("Farklı Kaydet");
        m1.add(m11);
        m1.add(m22);
        
        /*
       JButton button1 = new JButton("Button 1");
       JButton button2 = new JButton("Button 2");
       frame.getContentPane().add(button1);
       frame.getContentPane().add(button2);
       */
        JTextArea ta = new JTextArea();
        frame.getContentPane().add(BorderLayout.SOUTH, panel);
        frame.getContentPane().add(BorderLayout.NORTH, mb);
        frame.getContentPane().add(BorderLayout.CENTER, ta);
       frame.setVisible(true);

	}

	@Override
	public void actionPerformed(ActionEvent e) {
		// TODO Auto-generated method stub
		
	}

}

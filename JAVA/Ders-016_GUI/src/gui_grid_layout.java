import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.*;
public class gui_grid_layout {

	public static void main(String[] args) {
		JFrame f = new JFrame("GridBagLayout");
		JPanel MyPanel = new JPanel();
		MyPanel.setLayout( new GridBagLayout() );
		GridBagConstraints c = new GridBagConstraints();
	   	 
		JMenuBar mb = new JMenuBar();
		JMenu m1 = new JMenu("Dosya");
		JMenu m2 = new JMenu("Yardım");
		mb.add(m1);
		mb.add(m2);
		
		// Dosya menüsüne alt menü ekledik.
		JMenuItem m11 = new JMenuItem("Aç");
		JMenuItem m22 = new JMenuItem("Farklı Kaydet");
		m1.add(m11);
		m1.add(m22);
		c.fill = GridBagConstraints.HORIZONTAL;
		c.gridx = 0;
		c.gridy = 0;
		c.gridwidth = 4;
		MyPanel.add(mb,c);
		
	    
		JButton x1  = new JButton("Buton 1");
		c.fill = GridBagConstraints.HORIZONTAL;
		c.gridx = 0;
		c.gridy = 1;
		c.gridwidth = 1;
		MyPanel.add(x1,c);
		
		JButton x2  = new JButton("Buton 2");
		c.fill = GridBagConstraints.HORIZONTAL;
		c.gridx = 1;
		c.gridy = 1;
		MyPanel.add(x2,c);
		 
		JButton x3  = new JButton("Buton 3");
		c.fill = GridBagConstraints.HORIZONTAL;
		c.gridx = 2;
		c.gridy = 1;
		MyPanel.add(x3,c);
		 
		JButton x4  = new JButton("Buton 4");
		c.fill = GridBagConstraints.HORIZONTAL;
		c.gridx = 3;
		c.gridy = 1;
		MyPanel.add(x4,c);

		
		JLabel lbl_isim = new JLabel("Yazı giriniz: ");
		c.fill = GridBagConstraints.HORIZONTAL;
		c.gridx = 0;
		c.gridy = 3;
		MyPanel.add(lbl_isim,c);
		
        JTextField txt_isim = new JTextField(10); // accepts upto 10 characters
		c.fill = GridBagConstraints.HORIZONTAL;
		c.gridx = 1;
		c.gridy = 3;
		MyPanel.add(txt_isim,c);
		
		JButton btn_kontrol = new JButton("Kontrol");
		c.fill = GridBagConstraints.HORIZONTAL;
		c.gridx = 2;
		c.gridy = 3;
		MyPanel.add(btn_kontrol,c);
		
		JLabel lbl_sonuc = new JLabel("asdasdasdasd");
		lbl_sonuc.setBackground(Color.pink);
		lbl_sonuc.setSize(500,200);
		c.gridwidth = 4;
		c.gridheight = 2;
		c.fill = GridBagConstraints.HORIZONTAL;
		c.gridx = 0;
		c.gridy = 4;
		MyPanel.add(lbl_sonuc,c);
		
		btn_kontrol.addActionListener(new ActionListener()
	    {
		      public void actionPerformed(ActionEvent e)
		      {
		        
		    	/*
		        JDialog d = new JDialog(f, "Merhaba", true);
		        d.setLocationRelativeTo(f);
		        d.setVisible(true);
		        */
		        String isim = txt_isim.getText();
		        lbl_sonuc.setText(isim);
		        
		      }
		});
	   	f.getContentPane().add(MyPanel, "Center"); // Paste MyPanel into JFrame    
	   	f.setSize(500, 500);
	   	f.setVisible(true);

	}

}

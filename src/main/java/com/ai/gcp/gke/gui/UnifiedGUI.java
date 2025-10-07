package com.ai.gcp.gke.gui;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JScrollPane;
import javax.swing.JTextArea;

import org.json.JSONObject;

import com.ai.gcp.gke.repository.GKERepository;

public class UnifiedGUI {

	public static void main(String[] args) {

		JFrame frame = new JFrame("GKE Cluster Manager with AI");
		frame.setSize(700, 500);
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

		JTextArea textArea = new JTextArea();
		JButton btnFetch = new JButton("Fetch Clusters & AI Insights");

		btnFetch.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				String data = GKERepository.fetchClusters();
				JSONObject json = new JSONObject(data);

				StringBuilder display = new StringBuilder();
				display.append("=== Clusters ===\n");
				json.getJSONArray("clusters").forEach(c -> display.append(c.toString()).append("\n"));

				display.append("\n=== Anomalies ===\n");
				json.getJSONArray("anomalies").forEach(a -> display.append(a.toString()).append("\n"));

				display.append("\n=== Suggestions ===\n");
				json.getJSONArray("suggestions").forEach(s -> display.append(s.toString()).append("\n"));

				textArea.setText(display.toString());
			}
		});

		frame.getContentPane().add(btnFetch, "North");
		frame.getContentPane().add(new JScrollPane(textArea), "Center");

		frame.setVisible(true);
	}
}

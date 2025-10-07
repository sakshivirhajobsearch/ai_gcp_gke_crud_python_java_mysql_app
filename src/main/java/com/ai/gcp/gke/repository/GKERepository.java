package com.ai.gcp.gke.repository;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;

public class GKERepository {

	private static final String API_URL = "http://127.0.0.1:5000/gke/clusters";

	public static String fetchClusters() {
		try {
			URL url = new URL(API_URL);
			HttpURLConnection con = (HttpURLConnection) url.openConnection();
			con.setRequestMethod("GET");

			BufferedReader in = new BufferedReader(new InputStreamReader(con.getInputStream()));
			String inputLine;
			StringBuffer content = new StringBuffer();

			while ((inputLine = in.readLine()) != null) {
				content.append(inputLine);
			}

			in.close();
			con.disconnect();
			return content.toString();

		} catch (Exception e) {
			e.printStackTrace();
			return "{}";
		}
	}
}

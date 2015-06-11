package com.dotworld.bikerobada;

import android.app.Activity;
import android.content.Context;
import android.graphics.Color;
import android.net.ConnectivityManager;
import android.net.NetworkInfo;
import android.os.AsyncTask;
import android.os.Bundle;
import android.support.v7.app.ActionBarActivity;
import android.util.Log;
import android.view.View;
import android.widget.TextView;
import android.widget.Toast;

import org.apache.http.HttpResponse;
import org.apache.http.client.HttpClient;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.impl.client.DefaultHttpClient;
import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import com.dotworld.bikerobada2.R;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;

/**
 * Created by marcelo on 03/06/14.
 */
public class ShowResult extends ActionBarActivity {

    final Context context = this;

    TextView t1, t2, t3, t4, t5, t6, t7;
    TextView m1, m2, m3, m4, m5, m6;
    View s1, s2, s3, s4, s5;
    String ip;

    public static String GET(String url) {
        InputStream inputStream = null;
        String result = "";
        try {

            // create HttpClient
            HttpClient httpclient = new DefaultHttpClient();

            // make GET request to the given URL
            HttpResponse httpResponse = httpclient.execute(new HttpGet(url));

            // receive response as inputStream
            inputStream = httpResponse.getEntity().getContent();

            // convert inputstream to string
            if (inputStream != null)
                result = convertInputStreamToString(inputStream);
            else
                result = "Did not work!";

        } catch (Exception e) {
            //Log.d("InputStream", e.getLocalizedMessage());
        }

        return result;
    }

    private static String convertInputStreamToString(InputStream inputStream) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(inputStream));
        String line = "";
        String result = "";
        while ((line = bufferedReader.readLine()) != null)
            result += line;

        inputStream.close();
        return result;

    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_showresult);

        //Alert7Dialog.Builder alertBuilder = new AlertDialog.Builder(context);

        Bundle extras = getIntent().getExtras();

        String v1 = extras.getString("TV1");
        String v2 = extras.getString("TV2");

        t1 = (TextView) findViewById(R.id.textView2);
        t2 = (TextView) findViewById(R.id.textView3);
        t3 = (TextView) findViewById(R.id.datosBicicleta);
        t4 = (TextView) findViewById(R.id.datosVelocidades);
        t5 = (TextView) findViewById(R.id.numerosSerie);
        t6 = (TextView) findViewById(R.id.datosRobo);
        t7 = (TextView) findViewById(R.id.datosOtros);

        m1 = (TextView) findViewById(R.id.textView4);
        m2 = (TextView) findViewById(R.id.textView6);
        m3 = (TextView) findViewById(R.id.textView7);
        m4 = (TextView) findViewById(R.id.textView8);
        m5 = (TextView) findViewById(R.id.textView9);
        m6 = (TextView) findViewById(R.id.textView10);

        s1 = (View) findViewById(R.id.separator2);
        s2 = (View) findViewById(R.id.separator3);
        s3 = (View) findViewById(R.id.separator4);
        s4 = (View) findViewById(R.id.separator5);
        s5 = (View) findViewById(R.id.separator6);

        String FILENAME = "ipaddr";
        FileOutputStream fos = null;
        try {
            // open the file for reading
            BufferedReader fin =
                    new BufferedReader(new InputStreamReader(openFileInput(FILENAME)));

            ip = fin.readLine();
            //Log.d("InputStream", "USANDO LA IP:" + ip.toString());
            fin.close();
        } catch (Exception ex) {
           // Log.d("InputStream", "Error");
            ip = "dotworld.no-ip.info";
            File yourFile = new File("score.txt");
            if(!yourFile.exists()) {
                try {
                    fos = openFileOutput(FILENAME, Context.MODE_PRIVATE);
                    fos.write(ip.getBytes());
                    fos.close();
                } catch (java.io.IOException e) {
                    e.printStackTrace();
                }
            }

        }
        /* Formato de llegada de datos
           http://10.0.2.2:8080/query/raleigh/none/12331/9999 */
        if ("demorobo".equals(v1.toString())) {
            t1.setText("ROBO");
            t1.setTextColor(Color.WHITE);
            t2.setText("usuario@mail.com\n+54 11 4123 4321"); // return an article url
            t2.setTextColor(Color.WHITE);
            t1.setBackgroundColor(Color.RED);
            t2.setBackgroundColor(Color.RED);
            t2.setVisibility(View.VISIBLE);
            String datos1 =
                    "Marca: " + "Raleigh" + "\n" +
                    "Modelo: " + "Mohave 2.0" + "  " +
                    "Año: " + "2010" + "  " +
                    "Tipo: " + "MTB" + "\n" +
                    "Colores: " + "Negro y blanco" + "\n";

            String datos2 =
                    "Velocidades: " + "21" + "\n" +
                    "Marca Velocidades: " + "Shimano" + "\n" +
                    "Modelo Velocidades: " + "Alivio" + "\n";

            String datos3 =
                    "# cuadro: " + "314159265359" + "\n" +
                    "# horquilla: " + "1123581321345589" + "\n";

            String datos4 =
                    "Fecha Robo: " + "2014-01-01" + "\n" +
                    "Lugar Robo: " + "CABA" + "\n" +
                    "Lugar Denuncia: " + "Comisaria 0000" + "\n";
            String datos5 =
                    "Accesorios: " + "GPS Garmin" + "\n" +
                    "Detalle: " + " " + "\n" +
                    "Recompensa: " + "SI" + "\n" +
                    "Seguridad usada: " + "Atada con cadena";


            t3.setText(datos1);
            t4.setText(datos2);
            t5.setText(datos3);
            t6.setText(datos4);
            t7.setText(datos5);
        } else if ("demook".equals(v1.toString())) {
            t1.setText("OK");
            t1.setTextColor(Color.WHITE);
            t1.setBackgroundColor(Color.GREEN);
            t2.setVisibility(View.INVISIBLE);
            t2.setVisibility(View.INVISIBLE);
            m1.setVisibility(View.INVISIBLE);
            m2.setVisibility(View.INVISIBLE);
            m3.setVisibility(View.INVISIBLE);
            m4.setVisibility(View.INVISIBLE);
            m5.setVisibility(View.INVISIBLE);
            m6.setVisibility(View.INVISIBLE);
            s1.setVisibility(View.INVISIBLE);
            s2.setVisibility(View.INVISIBLE);
            s3.setVisibility(View.INVISIBLE);
            s4.setVisibility(View.INVISIBLE);
            s5.setVisibility(View.INVISIBLE);

        } else {
            String urlGet = "http://" + ip + ":8080/query/" + v1.toString() +
                    "/" + v2.toString();

            if(isConnected()){
                new HttpAsyncTask().execute(urlGet);
            }
            else{
                failGetRest();
            }
        }
    }

    private class HttpAsyncTask extends AsyncTask<String, Void, String> {
        @Override
        protected String doInBackground(String... urls) {

            return GET(urls[0]);
        }

        // onPostExecute displays the results of the AsyncTask.
        @Override
        protected void onPostExecute(String result) {

            JSONObject json = null; // convert String to JSONObject
            try {
                Toast.makeText(getBaseContext(), "Recibiendo datos...", Toast.LENGTH_LONG).show();
                json = new JSONObject(result);
                JSONArray resultset = json.getJSONArray("resultset"); // get articles array
                String estado = resultset.getJSONObject(0).getString("mensaje"); // return an article url
                t1.setText(estado);
                t1.setTextColor(Color.WHITE);
                t2.setTextColor(Color.WHITE);
                Log.d("InputStream", estado);
                if ("OK".equals(estado)) {
                    t1.setBackgroundColor(Color.GREEN);
                    t2.setVisibility(View.INVISIBLE);
                    m1.setVisibility(View.INVISIBLE);
                    m2.setVisibility(View.INVISIBLE);
                    m3.setVisibility(View.INVISIBLE);
                    m4.setVisibility(View.INVISIBLE);
                    m5.setVisibility(View.INVISIBLE);
                    m6.setVisibility(View.INVISIBLE);
                    s1.setVisibility(View.INVISIBLE);
                    s2.setVisibility(View.INVISIBLE);
                    s3.setVisibility(View.INVISIBLE);
                    s4.setVisibility(View.INVISIBLE);
                    s5.setVisibility(View.INVISIBLE);
                } else {
                    t2.setText(resultset.getJSONObject(0).getString("email") + "\n" +
                            "Telefono Contacto: " +
                            resultset.getJSONObject(0).getString("telefonoContacto") + "\n"); // return an article url
                    t1.setBackgroundColor(Color.RED);
                    t2.setBackgroundColor(Color.RED);
                    t2.setVisibility(View.VISIBLE);
                    t3.setVisibility(View.VISIBLE);
                    t3.setTextColor(Color.parseColor("#898889"));
                    m1.setVisibility(View.VISIBLE);
                    m2.setVisibility(View.VISIBLE);
                    m3.setVisibility(View.VISIBLE);
                    m4.setVisibility(View.VISIBLE);
                    m5.setVisibility(View.VISIBLE);
                    m6.setVisibility(View.VISIBLE);
                    s1.setVisibility(View.VISIBLE);
                    s2.setVisibility(View.VISIBLE);
                    s3.setVisibility(View.VISIBLE);
                    s4.setVisibility(View.VISIBLE);
                    s5.setVisibility(View.VISIBLE);
                    String datos1 =
                            "Marca: " + resultset.getJSONObject(0).getString("marca") + "\n" +
                            "Modelo: " + resultset.getJSONObject(0).getString("modelo") + "  " +
                            "Año: " + resultset.getJSONObject(0).getString("anioModelo") + "  " +
                            "Tipo: " + resultset.getJSONObject(0).getString("tipo") + "\n" +
                            "Colores: " + resultset.getJSONObject(0).getString("colores") + "\n";

                    String datos2 =
                            "Velocidades: " + resultset.getJSONObject(0).getString("modelo") + "\n" +
                            "Marca Velocidades: " + resultset.getJSONObject(0).getString("marcaVelocidades") + "\n" +
                            "Modelo Velocidades: " + resultset.getJSONObject(0).getString("modeloVelocidades") + "\n";

                    String datos3 =
                            "# cuadro: " + resultset.getJSONObject(0).getString("nrocuadro") + "\n" +
                            "# horquilla: " + resultset.getJSONObject(0).getString("nrohorquilla") + "\n";

                    String datos4 =
                            "Fecha Robo: " + resultset.getJSONObject(0).getString("fechaRobo") + "\n" +
                            "Lugar Robo: " + resultset.getJSONObject(0).getString("lugarRobo") + "\n" +
                            "Lugar Denuncia: " + resultset.getJSONObject(0).getString("lugarDenuncia") + "\n";

                    String datos5 =
                            "Accesorios: " + resultset.getJSONObject(0).getString("accesorios") + "\n" +
                            "Detalle: " + resultset.getJSONObject(0).getString("detalle") + "\n" +
                            "Recompensa: " + resultset.getJSONObject(0).getString("recompensa") + "\n" +
                            "Seguridad usada: " + resultset.getJSONObject(0).getString("condicion");

                    t3.setText(datos1);
                    t4.setText(datos2);
                    t5.setText(datos3);
                    t6.setText(datos4);
                    t7.setText(datos5);
                }
            } catch (JSONException e) {
                failGetRest();
                e.printStackTrace();
            }
        }
    }

    public boolean isConnected(){
        ConnectivityManager connMgr = (ConnectivityManager) getSystemService(Activity.CONNECTIVITY_SERVICE);
        NetworkInfo networkInfo = connMgr.getActiveNetworkInfo();
        if (networkInfo != null && networkInfo.isConnected())
            return true;
        else
            return false;
    }

    protected void failGetRest(){
        t1.setText("URL de consulta no valida.");
        t1.setTextColor(Color.YELLOW);
        t1.setBackgroundColor(Color.RED);
        t2.setVisibility(View.INVISIBLE);
        t2.setVisibility(View.INVISIBLE);
        m1.setVisibility(View.INVISIBLE);
        m2.setVisibility(View.INVISIBLE);
        m3.setVisibility(View.INVISIBLE);
        m4.setVisibility(View.INVISIBLE);
        m5.setVisibility(View.INVISIBLE);
        m6.setVisibility(View.INVISIBLE);
        s1.setVisibility(View.INVISIBLE);
        s2.setVisibility(View.INVISIBLE);
        s3.setVisibility(View.INVISIBLE);
        s4.setVisibility(View.INVISIBLE);
        s5.setVisibility(View.INVISIBLE);
    }
}


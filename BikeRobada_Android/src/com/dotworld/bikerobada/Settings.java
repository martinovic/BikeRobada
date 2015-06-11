package com.dotworld.bikerobada;

import android.content.Context;
import android.os.Bundle;
import android.support.v7.app.ActionBarActivity;
import android.util.Log;
import android.view.View;
import android.widget.EditText;
import android.widget.ImageButton;
import android.widget.Toast;

import java.io.BufferedReader;
import java.io.FileOutputStream;
import java.io.InputStreamReader;

import com.dotworld.bikerobada2.R;

public class Settings extends ActionBarActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_settings);
        EditText inputData = (EditText) findViewById(R.id.editText);
        try {
            // open the file for reading
            String FILENAME = "ipaddr";
            BufferedReader fin =
                    new BufferedReader(new InputStreamReader(openFileInput(FILENAME)));

            String texto = fin.readLine();
            inputData.setText(texto);
            Log.d("InputStream", texto.toString());
            fin.close();
        } catch (Exception ex) {
            Log.d("InputStream", "Error");
        }

        addBtnListener();
    }

    public void addBtnListener() {
        ImageButton btn = (ImageButton) findViewById(R.id.buttonSaveSetting);

        btn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                /*DateFormat dateFormat = new SimpleDateFormat("yyyy/MM/dd HH:mm:ss");
                Date date = new Date();
                System.out.println(dateFormat.format(date));*/

                EditText inputData = (EditText) findViewById(R.id.editText);

                String FILENAME = "ipaddr";
                String string = inputData.getText().toString();
                FileOutputStream fos = null;
                try {
                    fos = openFileOutput(FILENAME, Context.MODE_PRIVATE);
                    fos.write(string.getBytes());
                    fos.close();
                    Toast.makeText(getBaseContext(), "Grabado !!!", Toast.LENGTH_LONG).show();
                } catch (java.io.IOException e) {
                    e.printStackTrace();
                }
                //Log.d("InputStream", "Entrando");
                /*try {
                    // open the file for reading
                    BufferedReader fin =
                            new BufferedReader(new InputStreamReader(openFileInput(FILENAME)));

                    String texto = fin.readLine();
                    Log.d("InputStream", texto.toString());
                    fin.close();
                } catch (Exception ex) {
                    Log.d("InputStream", "Error");
                }*/
                //Log.d("InputStream", "Salio");
            }
        });
    }

/*    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.settings, menu);
        return true;
    }*/
/*
    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        // Handle action bar item clicks here. The action bar will
        // automatically handle clicks on the Home/Up button, so long
        // as you specify a parent activity in AndroidManifest.xml.
        int id = item.getItemId();
        if (id == R.id.action_settings) {
            return true;
        }
        return super.onOptionsItemSelected(item);
    }*/
}

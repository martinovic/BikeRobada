package com.dotworld.bikerobada;

import com.dotworld.bikerobada2.R;

import android.content.Context;
import android.content.Intent;
import android.os.Bundle;
import android.support.v7.app.ActionBarActivity;
import android.util.Log;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.widget.EditText;
import android.widget.ImageButton;
import android.widget.TextView;

public class MainActivity extends ActionBarActivity {

    EditText nroCuadro, nroHorquilla;

    EditText etResponse;
    TextView tvIsConnected;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        final Context context = this;

        nroCuadro = (EditText) findViewById(R.id.nroCuadro);
        nroHorquilla = (EditText) findViewById(R.id.nroHorquilla);

        ImageButton addBtn = (ImageButton) findViewById(R.id.boton1);

        addBtn.setOnClickListener(new View.OnClickListener() {

            @Override
            public void onClick(View view) {
                //textoValor1.setText(new Date().toString());
                Intent intent = new Intent(getApplicationContext(), ShowResult.class);
                intent.putExtra("TV1", nroCuadro.getText().toString());
                intent.putExtra("TV2", nroHorquilla.getText().toString());
                startActivity(intent);
            }

        });

    }

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.main, menu);
        return true;
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        // Handle action bar item clicks here. The action bar will
        // automatically handle clicks on the Home/Up button, so long
        // as you specify a parent activity in AndroidManifest.xml.
        int id = item.getItemId();
        if (id == R.id.settings) {
            Log.d("InputStream", "Configuracion");
            Intent intent = new Intent(this, Settings.class);
            startActivity(intent);
            return true;
        }

        if (id == R.id.legales) {
            Log.d("InputStream", "Informacion");
            Intent intent = new Intent(this, Legales.class);
            startActivity(intent);
            return true;
        }
        if (id == R.id.informacion) {
            Log.d("InputStream", "Legales");
            Intent intent = new Intent(this, Informacion.class);
            startActivity(intent);
            return true;
        }
        if (id == R.id.manualuso) {
            Log.d("InputStream", "Manual de uso");
            Intent intent = new Intent(this, ManualUso.class);
            startActivity(intent);
            return true;
        }

        if (id == R.id.salir) {
            super.finish();
        }

        return super.onOptionsItemSelected(item);
    }

}
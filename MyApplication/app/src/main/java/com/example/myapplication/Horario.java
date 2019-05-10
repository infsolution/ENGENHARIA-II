package com.example.myapplication;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.TextView;

public class Horario extends AppCompatActivity {
    private TextView sext_01;
    private TextView sext_04;
    private TextView sext_05;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_horario);
        sext_01 = (TextView) findViewById(R.id.tv_sexta_01);
        sext_04 = (TextView) findViewById(R.id.tv_sexta_04);
        sext_05 = (TextView) findViewById(R.id.tv_sexta_05);

    }

    public void goSxt1(View v){
        Intent go = new Intent(this, DetalheDia.class);
        go.putExtra("Disciplina", "Engenharia");
        go.putExtra("Disciplina", "Hécio");
        startActivity(go);
    }
    public void goSxt4(View v){
        Intent go = new Intent(this, DetalheDia.class);
        go.putExtra("Disciplina", "Tópicos");
        go.putExtra("Disciplina", "Ely");
        startActivity(go);
    }
    public void goSxt5(View v){
        Intent go = new Intent(this, DetalheDia.class);
        go.putExtra("Disciplina", "Ely");
        startActivity(go);
    }
}

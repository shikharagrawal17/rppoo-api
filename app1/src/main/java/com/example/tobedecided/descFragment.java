package com.example.tobedecided;

import android.os.Bundle;

import androidx.appcompat.app.AppCompatActivity;
import androidx.fragment.app.Fragment;

import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ImageView;
import android.widget.TextView;

import com.bumptech.glide.Glide;

public class descFragment extends Fragment {

    private static final String ARG_PARAM1 = "param1";
    private static final String ARG_PARAM2 = "param2";

    String Name, AverageSalary, Logo, Placements, Rounds;
    private String mParam1;
    private String mParam2;

    public descFragment(String Name, String AverageSalary, String Logo, String Placements, String Rounds) {
        this.Name = Name;
        this.AverageSalary = AverageSalary;
        this.Logo = Logo;
        this.Placements = Placements;
        this.Rounds = Rounds;

    }

    public descFragment() {

    }


    public static descFragment newInstance(String param1, String param2) {
        descFragment fragment = new descFragment();
        Bundle args = new Bundle();
        args.putString(ARG_PARAM1, param1);
        args.putString(ARG_PARAM2, param2);
        fragment.setArguments(args);
        return fragment;
    }

    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        if (getArguments() != null) {
            mParam1 = getArguments().getString(ARG_PARAM1);
            mParam2 = getArguments().getString(ARG_PARAM2);
        }
    }

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {
         View view = inflater.inflate(R.layout.fragment_desc, container, false);

        ImageView imageholder = view.findViewById(R.id.imageholder);
        TextView nameholder = view.findViewById(R.id.nameholder);
        TextView avrSalHholder = view.findViewById(R.id.avrSalHolder);
        TextView placements = view.findViewById(R.id.placements);
        TextView rounds = view.findViewById(R.id.rounds);

        nameholder.setText(Name);
        avrSalHholder.setText(AverageSalary);
        placements.setText(Placements);
        rounds.setText(Rounds);
        Glide.with(getContext()).load(Logo).into(imageholder);
         return view;
    }

    public void onBackPressed(){
        AppCompatActivity activity = (AppCompatActivity)getContext();
        activity.getSupportFragmentManager().beginTransaction().replace(R.id.wrapper, new MainFragment()).addToBackStack(null).commit();

    }
}
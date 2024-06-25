package mypackage.sampleapp;

import javafx.fxml.FXML;
import javafx.application.Platform;
import javafx.scene.control.Label;
import javafx.event.ActionEvent;

public class HelloController {
    @FXML
    private Label welcomeText;

    @FXML
    protected void onHelloButtonClick() {
        welcomeText.setText("Welcome to JavaFX Application!");
    }

    @FXML
    protected void onQuitClicked(ActionEvent event) {Platform.exit();}

    @FXML 
    protected void handlePlay() {
        welcomeText.setText("Test 1");
    }

    @FXML 
    protected void handlePause() {
        welcomeText.setText("Test 2");
    }

    @FXML 
    protected void handleStop() {
        welcomeText.setText("Test 3");
    }

    @FXML 
    protected void handleSeek() {
        welcomeText.setText("Test 4");
    }


}
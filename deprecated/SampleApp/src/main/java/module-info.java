module mypackage.sampleapp {
    requires javafx.controls;
    requires javafx.fxml;
    requires javafx.media;


    opens mypackage.sampleapp to javafx.fxml;
    exports mypackage.sampleapp;
}
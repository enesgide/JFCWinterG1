module mypackage.sampleapp {
    requires javafx.controls;
    requires javafx.fxml;


    opens mypackage.sampleapp to javafx.fxml;
    exports mypackage.sampleapp;
}
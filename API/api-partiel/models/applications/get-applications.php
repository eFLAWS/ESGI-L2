<?php

include __DIR__ . "/../../functions/get-database-connection.php";

function getApplications() {
    $databaseConnection = getDatabaseConnection();
    $query = $databaseConnection->query("SELECT * FROM applications;");
    $applications = $query->fetchAll();

    return $applications;
}

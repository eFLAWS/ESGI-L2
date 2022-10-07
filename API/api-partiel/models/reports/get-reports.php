<?php

include __DIR__ . "/../../functions/get-database-connection.php";

function getReports() {
    $databaseConnection = getDatabaseConnection();
    $query = $databaseConnection->query("SELECT * FROM reports;");
    $reports = $query->fetchAll();

    return $reports;
}

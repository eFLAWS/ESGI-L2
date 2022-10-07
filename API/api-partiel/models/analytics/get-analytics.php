<?php

include __DIR__ . "/../../functions/get-database-connection.php";

function getAnalytics() {
    $databaseConnection = getDatabaseConnection();
    $query = $databaseConnection->query("SELECT * FROM analytics;");
    $analytics = $query->fetchAll();

    return $analytics;
}

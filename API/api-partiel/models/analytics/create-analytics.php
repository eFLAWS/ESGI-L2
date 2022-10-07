<?php

include __DIR__ . "/../../functions/get-database-connection.php";

function createAnalytics($analytics) {
    $databaseConnection = getDatabaseConnection();
    $query = $databaseConnection->prepare("INSERT INTO analytics(name, value, report) VALUES(:name, :value, :report)");
    $query->execute($analytics);
}
<?php

include __DIR__ . "/../../functions/get-database-connection.php";

function createReports($reports) {
    $databaseConnection = getDatabaseConnection();
    $query = $databaseConnection->prepare("INSERT INTO reports(name, description, reporter, application) VALUES(:name, :description, :reporter, :application)");
    $query->execute($reports);
}
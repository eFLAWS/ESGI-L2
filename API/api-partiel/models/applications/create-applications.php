<?php

include __DIR__ . "/../../functions/get-database-connection.php";

function createApplications($applications) {
    $databaseConnection = getDatabaseConnection();
    $query = $databaseConnection->prepare("INSERT INTO applications(name) VALUES(:name)");
    $query->execute($applications);
}
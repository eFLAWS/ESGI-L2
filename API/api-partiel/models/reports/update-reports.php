<?php

include __DIR__ . "/../../functions/get-database-connection.php";

function updateReports($body) {
    $set = [];

    foreach ($body as $key => $value) {
        if ($key === "id") {
            continue;
        }
        
        $set[] = "$key = :$key";
    }

    $set = implode(", ", $set);
    $databaseConnection = getDatabaseConnection();
    $query = $databaseConnection->prepare("UPDATE reports SET $set WHERE id = :id;");
    $query->execute($body);
}

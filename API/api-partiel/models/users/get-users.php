<?php

include __DIR__ . "/../../functions/get-database-connection.php";

function getUsers() {
    $databaseConnection = getDatabaseConnection();
    $query = $databaseConnection->query("SELECT * FROM users;");
    $users = $query->fetchAll();

    return $users;
}

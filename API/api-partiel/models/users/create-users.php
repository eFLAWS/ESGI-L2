<?php

include __DIR__ . "/../../functions/get-database-connection.php";

function createUsers($users) {
    $databaseConnection = getDatabaseConnection();
    $query = $databaseConnection->prepare("INSERT INTO users(email, password, token, role) VALUES(:email, :password, :token, :role)");
    $query->execute($users);
}
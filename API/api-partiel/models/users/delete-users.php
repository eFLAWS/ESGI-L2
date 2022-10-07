<?php

include __DIR__ . "/../../functions/get-database-connection.php";

function deleteUsers($id) {
    $databaseConnection = getDatabaseConnection();
    $query = $databaseConnection->prepare("DELETE FROM users WHERE id = :id");
    $query->execute(["id" => $id]);
}
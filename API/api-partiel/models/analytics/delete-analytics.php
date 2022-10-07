<?php

include __DIR__ . "/../../functions/get-database-connection.php";

function deleteAnalytics($id) {
    $databaseConnection = getDatabaseConnection();
    $query = $databaseConnection->prepare("DELETE FROM analytics WHERE id = :id");
    $query->execute(["id" => $id]);
}
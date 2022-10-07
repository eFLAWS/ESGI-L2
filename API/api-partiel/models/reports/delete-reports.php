<?php

include __DIR__ . "/../../functions/get-database-connection.php";

function deleteReports($id) {
    $databaseConnection = getDatabaseConnection();
    $query = $databaseConnection->prepare("DELETE FROM reports WHERE id = :id");
    $query->execute(["id" => $id]);
}
<?php

include __DIR__ . "/../../functions/get-database-connection.php";

function deleteApplications($id) {
    $databaseConnection = getDatabaseConnection();
    $query = $databaseConnection->prepare("DELETE FROM applications WHERE id = :id");
    $query->execute(["id" => $id]);
}
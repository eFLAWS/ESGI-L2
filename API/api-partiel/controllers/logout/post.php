<?php
/*
include __DIR__ . "/../../functions/json-response.php";
include __DIR__ . "/../../functions/get-json-body.php";
include __DIR__ . "/../../models/logout/create-logout.php";

try {

    $body = getJsonBody();

    createLogout([
        "id" => $body->id,
        "password" => $body->password,
    ]);

    jsonResponse(201, [], ["success" => true]);
} catch (PDOException $exception) {
    $errorMessage = $exception->getMessage();
    jsonResponse(500, [], ["success" => false, "error" => "Error while trying to access the dabtabase: $errorMessage"]);
}
*/
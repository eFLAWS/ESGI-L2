<?php

include __DIR__ . "/../../functions/json-response.php";
include __DIR__ . "/../../functions/get-json-body.php";
include __DIR__ . "/../../models/users/create-users.php";

try {

    $body = getJsonBody();

    createUsers([
        "email" => $body->email,
        "password" => $body->password,
        "token" => $body->token,
        "role" => $body->role
    ]);

    jsonResponse(201, [], ["success" => true]);
} catch (PDOException $exception) {
    $errorMessage = $exception->getMessage();
    jsonResponse(500, [], ["success" => false, "error" => "Error while trying to access the dabtabase: $errorMessage"]);
}

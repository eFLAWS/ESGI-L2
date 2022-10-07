<?php

include __DIR__ . "/../../functions/json-response.php";
include __DIR__ . "/../../functions/get-json-body.php";
include __DIR__ . "/../../models/users/update-users.php";

try {
    $body = getJsonBody(true);

    updateUsers($body);

    jsonResponse(200, [], ["success" => true]);
}

catch (PDOException $exception) {
    $errorMessage = $exception->getMessage();

    jsonResponse(500, [], ["success" => false, "error" => "Error while trying to access the dabtabase: $errorMessage"]);
}
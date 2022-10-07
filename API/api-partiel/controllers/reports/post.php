<?php

include __DIR__ . "/../../functions/json-response.php";
include __DIR__ . "/../../functions/get-json-body.php";
include __DIR__ . "/../../models/reports/create-reports.php";

try {

    $body = getJsonBody();

    createReports([
        "name" => $body->name,
        "description" => $body->description,
        "reporter" => $body->reporter,
        "application" => $body->application
    ]);

    jsonResponse(201, [], ["success" => true]);
} catch (PDOException $exception) {
    $errorMessage = $exception->getMessage();
    jsonResponse(500, [], ["success" => false, "error" => "Error while trying to access the dabtabase: $errorMessage"]);
}

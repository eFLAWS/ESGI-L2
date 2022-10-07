<?php

include __DIR__ . "/../../functions/json-response.php";
include __DIR__ . "/../../functions/get-json-body.php";
include __DIR__ . "/../../models/analytics/create-analytics.php";

try {

    $body = getJsonBody();

    createAnalytics([
        "name" => $body->name,
        "value" => $body->value,
        "report" => $body->report,
    ]);

    jsonResponse(201, [], ["success" => true]);
} catch (PDOException $exception) {
    $errorMessage = $exception->getMessage();
    jsonResponse(500, [], ["success" => false, "error" => "Error while trying to access the dabtabase: $errorMessage"]);
}

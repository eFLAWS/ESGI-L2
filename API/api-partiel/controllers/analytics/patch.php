<?php

include __DIR__ . "/../../functions/json-response.php";
include __DIR__ . "/../../functions/get-json-body.php";
include __DIR__ . "/../../models/analytics/update-analytics.php";

try {
    $body = getJsonBody(true);

    updateAnalytics($body);

    jsonResponse(200, [], ["success" => true]);
}

catch (PDOException $exception) {
    $errorMessage = $exception->getMessage();

    jsonResponse(500, [], ["success" => false, "error" => "Error while trying to access the dabtabase: $errorMessage"]);
}
<?php

include __DIR__ . "/../../functions/json-response.php";
include __DIR__ . "/../../models/analytics/get-analytics.php";

try {
    $analytics = getAnalytics();
    jsonResponse(200, [], ["success" => true, "analytics" => $analytics]);
} 

catch (PDOException $exception) {
    $errorMessage = $exception->getMessage();

    jsonResponse(500, [], ["success" => false, "error" => "Error while trying to access the dabtabase: $errorMessage"]);
}


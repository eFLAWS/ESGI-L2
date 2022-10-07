<?php

include __DIR__ . "/../../functions/json-response.php";
include __DIR__ . "/../../models/reports/get-reports.php";

try {
    $reports = getReports();
    jsonResponse(200, [], ["success" => true, "reports" => $reports]);
} 

catch (PDOException $exception) {
    $errorMessage = $exception->getMessage();

    jsonResponse(500, [], ["success" => false, "error" => "Error while trying to access the dabtabase: $errorMessage"]);
}


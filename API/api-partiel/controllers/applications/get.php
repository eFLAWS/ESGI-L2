<?php

include __DIR__ . "/../../functions/json-response.php";
include __DIR__ . "/../../models/applications/get-applications.php";

try {
    $applications = getApplications();
    jsonResponse(200, [], ["success" => true, "applications" => $applications]);
} 

catch (PDOException $exception) {
    $errorMessage = $exception->getMessage();

    jsonResponse(500, [], ["success" => false, "error" => "Error while trying to access the dabtabase: $errorMessage"]);
}


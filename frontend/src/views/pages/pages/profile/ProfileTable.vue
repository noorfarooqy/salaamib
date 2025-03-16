<template>
  <div class="col-lg-4">
    <div class="card card-body">
      <h5>Complete your profile</h5>

      <!-- Progress -->
      <div class="d-flex justify-content-between align-items-center">
        <div class="progress progress-md flex-grow-1">
          <div
            class="progress-bar bg-primary"
            role="progressbar"
            style="width: 30%"
            aria-valuenow="30"
            aria-valuemin="0"
            aria-valuemax="100"
          ></div>
        </div>
        <span class="ms-4">30%</span>
      </div>
      <!-- /Progress -->
    </div>

    <div class="card">
      <div class="card-header">
        <h5 class="card-title d-flex justify-content-between">
          <span>Profile</span>
          <router-link class="btn btn-sm btn-white" to="/settings/">Edit</router-link>
        </h5>
      </div>
      <div class="card-body">
        <ul class="list-unstyled mb-0">
          <li class="py-0">
            <h6>About</h6>
          </li>
          <li>Charles Hafner</li>
          <li>Hafner Pvt Ltd.</li>
          <li class="pt-2 pb-0">
            <h6 class="text-dark">Contacts</h6>
          </li>
          <li>charleshafner@example.com</li>
          <li>+1 (304) 499-13-66</li>
          <li class="pt-2 pb-0">
            <h6 class="text-dark">Address</h6>
          </li>
          <li>
            4663 Agriculture Lane,<br />
            Miami,<br />
            Florida - 33165,<br />
            United States.
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>
